/***************************************************************************//**
 * @file
 * @brief USB Host Example - Mass Storage Class (MSC)
 *******************************************************************************
 * # License
 * <b>Copyright 2018 Silicon Laboratories Inc. www.silabs.com</b>
 *******************************************************************************
 *
 * The licensor of this software is Silicon Laboratories Inc.  Your use of this
 * software is governed by the terms of Silicon Labs Master Software License
 * Agreement (MSLA) available at
 * www.silabs.com/about-us/legal/master-software-license-agreement.  This
 * software is distributed to you in Source Code format and is governed by the
 * sections of the MSLA applicable to Source Code.
 *
 ******************************************************************************/

/********************************************************************************************************
 * The MSC class driver is meant to be used with devices such as flash drives, external hard drives, media
 * card readers, CD-ROM readers, etc.
 *
 * This example requires the FS SCSI module.
 *******************************************************************************************************/

/********************************************************************************************************
 ********************************************************************************************************
 *                                     DEPENDENCIES & AVAIL CHECK(S)
 ********************************************************************************************************
 *******************************************************************************************************/

#include <rtos_description.h>

#if (defined(RTOS_MODULE_USB_HOST_MSC_AVAIL))

/********************************************************************************************************
 ********************************************************************************************************
 *                                            INCLUDE FILES
 ********************************************************************************************************
 *******************************************************************************************************/

#define   EX_USBH_MSC_MODULE

#include  <rtos_description.h>
#include  <cpu/include/cpu.h>
#include  <common/include/rtos_utils.h>
#include  <common/include/rtos_err.h>
#include  <common/include/lib_mem.h>

#include  <usb/include/host/usbh_core.h>
#include  <usb/include/host/usbh_msc.h>

#ifdef RTOS_MODULE_FS_STORAGE_SCSI_AVAIL
#include  <fs/include/fs_scsi.h>
#endif

#include  <ex_description.h>

/********************************************************************************************************
 ********************************************************************************************************
 *                                            LOCAL DEFINES
 ********************************************************************************************************
 *******************************************************************************************************/

/********************************************************************************************************
 ********************************************************************************************************
 *                                          LOCAL DATA TYPES
 ********************************************************************************************************
 *******************************************************************************************************/

/********************************************************************************************************
 ********************************************************************************************************
 *                                        LOCAL GLOBAL VARIABLES
 ********************************************************************************************************
 *******************************************************************************************************/

/********************************************************************************************************
 ********************************************************************************************************
 *                                      LOCAL FUNCTION PROTOTYPES
 ********************************************************************************************************
 *******************************************************************************************************/

/********************************************************************************************************
 ********************************************************************************************************
 *                                          LOCAL CONSTANTS
 ********************************************************************************************************
 *******************************************************************************************************/

#ifdef RTOS_MODULE_FS_STORAGE_SCSI_AVAIL
static const USBH_MSC_CMD_BLK_FNCTS Ex_USBH_MSC_CmdBlkFncts = { .Conn = FS_SCSI_LU_Conn,
                                                                .Disconn = FS_SCSI_LU_Disconn,
                                                                .MaxRespBufLenGet = FS_SCSI_MaxRespBufLenGet };
#endif

/********************************************************************************************************
 ********************************************************************************************************
 *                                          GLOBAL FUNCTIONS
 ********************************************************************************************************
 *******************************************************************************************************/

/****************************************************************************************************//**
 *                                           Ex_USBH_HID_Init()
 *
 * @brief  Example of initialization of the HID class driver.
 *******************************************************************************************************/
void Ex_USBH_MSC_Init(void)
{
#ifdef RTOS_MODULE_FS_STORAGE_SCSI_AVAIL
  RTOS_ERR err;

  USBH_MSC_Init(&Ex_USBH_MSC_CmdBlkFncts, &err);
  APP_RTOS_ASSERT_CRITICAL(err.Code == RTOS_ERR_NONE,; );
#endif
}

/********************************************************************************************************
 ********************************************************************************************************
 *                                   DEPENDENCIES & AVAIL CHECK(S) END
 ********************************************************************************************************
 *******************************************************************************************************/

#endif // RTOS_MODULE_USB_HOST_MSC_AVAIL